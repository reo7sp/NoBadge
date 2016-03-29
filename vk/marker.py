import time
import vk_api


def run_loop(token, delay=60, additional_ban_list=set()):
    session = vk_api.VkApi(token=token)
    vk = session.get_api()

    while True:
        for dialog in vk.messages.getDialogs(unread=1, count=200)["items"]:
            message = dialog["message"]

            is_to_mute = False
            if "push_settings" in message and "disabled_until" in message["push_settings"]:
                is_to_mute = True
            elif "chat_id" in message and message["chat_id"] in additional_ban_list:
                is_to_mute = True
            elif message["user_id"] in additional_ban_list:
                is_to_mute = True

            if is_to_mute:
                vk.messages.markAsRead(message_ids=message["id"])

        time.sleep(delay)
