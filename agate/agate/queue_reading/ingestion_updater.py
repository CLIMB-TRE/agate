import logging
from agate.models import IngestionAttempt
from agate.forms import IngestionAttemptForm

logger = logging.getLogger(__name__)


class IngestionUpdater:
    """
    This class interprets a dictionary (as may come from a rabbitMQ message)
    and creates or updates an IngestionAttempt appropriately.
    """

    @classmethod
    def update(cls, data: dict, stage: str):
        """
        Use a dictionary to update items in the database
        """
        try:
            uuid = data["uuid"]
        except KeyError:
            logger.fatal("no uuid")
            return
        cls._manipulate_data(data, stage)
        cls._update_item(uuid, data)

    @classmethod
    def _name(cls, data: dict, stage: str):
        """
        The user-facing name for this ingestion attempt
        """
        return "ToBeDecided"

    @classmethod
    def _manipulate_data(cls, data: dict, stage: str):
        """
        Tweak some dictionary keynames so they match the fields of the django database
        """
        data["status"] = cls._status(data, stage)
        data["name"] = cls._name(data, stage)
        data["is_published"] = data.get("published", False)
        data["is_test_attempt"] = data["test_flag"]
        data["error_message"] = str(data.get("onyx_test_create_errors", ""))

    @classmethod
    def _update_item(cls, uuid: str, data: dict):
        """
        Create or update the django database item
        """
        try:
            instance = IngestionAttempt.objects.get(uuid=uuid)
            form = IngestionAttemptForm(data, instance=instance)
        except IngestionAttempt.DoesNotExist:
            # IngestionAttempt doesn't exists, so we create a new one
            form = IngestionAttemptForm(data)
        if form.is_valid():
            form.save()
        else:
            logger.fatal(f"invalid ingestion attempt message: {form.errors}")

    @classmethod
    def _status(cls, data: dict, stage: str):
        """
        Interpret the data and current stage as a status enumerable
        """
        match stage:
            case "inbound-s3":
                return IngestionAttempt.Status.UNSTARTED
            case 'inbound-matched':
                return IngestionAttempt.Status.METADATA
            case 'inbound-to-validate':
                return IngestionAttempt.Status.VALIDATION
            case 'inbound-results':
                if (not data["validate"]):
                    return IngestionAttempt.Status.VALIDATIONFAIL
                else:
                    return IngestionAttempt.Status.SUCCESS
            case _:
                return IngestionAttempt.Status.UNSTARTED
