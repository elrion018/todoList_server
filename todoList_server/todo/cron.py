from pyfcm import FCMNotification
from account.models import Account
from todo.models import ToDo
import datetime
import logging

logger = logging.getLogger(__name__)


def push_messaging():
    todo = ToDo.object.filter(goal_date=str(
        datetime.datetime.now())[:10]+" 00:00:00.000000")
    logger.debug("test")
    return print(todo)


push_messaging()
# for _ in todo:
#     push_service = FCMNotification(
#         api_key="AAAAMZoXqpo:APA91bH-R5caFaI4FF4dcm9dE-LYGyOw0uzdl3Ww3Oi7tmU6-Kf9i9AGE2rm3ERv0C7vR4J3FtlMqGVqxBrEymWZCHJJ6_VUoO8VBe3XL_zO9wb9T4gxuNMnryj5fcaYMXgXb-Cjy5fH")

#     registration_id = "dY-KimkwQf0:APA91bHB-_xB8_N1AuMqGESaDyk3ZMpkgtSbxKj0ABVFH7UM0nof_9p5_tYXVDqzNBjno1NnkM9ZopFqmaDsoW9-So9lBD1sOhq9gRka7j-g1-zF8bM_RnJcBl38xrrybFNXGfQu6aVF"
#     message_title = "Uber update"
#     message_body = "Hi john, your customized news for today is ready"
#     result = push_service.notify_single_device(
#         registration_id=registration_id, message_title=message_title, message_body=message_body)
#     print(result)
