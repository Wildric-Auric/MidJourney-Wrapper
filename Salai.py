import Globals
import requests


def passPromptToSelfBot(prompt: str) -> requests.Response:
    """
    Sends a given prompt to the self bot for processing.

    Args:
        prompt (str): The prompt to be sent to the self bot.

    Returns:
        requests.Response: The response from the self bot.
    """
    payload = {
        "type": 2,
        "application_id": "936929561302675456",
        "guild_id": Globals.SERVER_ID,
        "channel_id": Globals.CHANNEL_ID,
        "session_id": "0a010c9eaf31b12c8b2345c0d38bbb7c",
        "data": {
            "version": "994261739745050686",
            "id": "938956540159881230",
            "name": "imagine",
            "type": 1,
            "options": [{"type": 3, "name": "prompt", "value": prompt}],
            "application_command": {
                "id": "938956540159881230",
                "application_id": "936929561302675456",
                "version": "994261739745050686",
                "default_permission": True,
                "default_member_permissions": None,
                "type": 1,
                "name": "imagine",
                "description": "There are endless possibilities...",
                "dm_permission": True,
                "options": [
                    {"type": 3, "name": "prompt", "description": "The prompt to imagine", "required": True}
                ],
            },
            "attachments": [],
        },
    }

    headers = {"authorization": Globals.SALAI_TOKEN}
    return requests.post("https://discord.com/api/v9/interactions", json=payload, headers=headers)


def upscale(index: int, message_id: str, message_hash: str) -> requests.Response:
    """
    Sends a request to the self bot to upscale an image.

    Args:
        index (int): The index of the image to be upscaled.
        message_id (str): The ID of the message containing the image.
        message_hash (str): The hash of the message containing the image.

    Returns:
        requests.Response: The response from the self bot.
    """

    payload = {
        "type": 3,
        "guild_id": Globals.SERVER_ID,
        "channel_id": Globals.CHANNEL_ID,
        "message_flags": 0,
        "message_id": message_id,
        "application_id": "936929561302675456",
        "session_id": "45bc04dd4da37141a5f73dfbfaf5bdcf",
        "data": {
            "component_type": 2,
            "custom_id": f"MJ::JOB::upsample::{index}::{message_hash}",
        },
    }
    headers = {"authorization": Globals.SALAI_TOKEN}
    return requests.post("https://discord.com/api/v9/interactions", json=payload, headers=headers)


def reroll(message_id: str, message_hash: str) -> requests.Response:
    """
    Sends a request to the self bot to generate a new image.

    Args:
        message_id (str): The ID of the message containing the image.
        message_hash (str): The hash of the message containing the image.

    Returns:
        requests.Response: The response from the self bot.
    """
    payload = {
        "type": 3,
        "guild_id": Globals.SERVER_ID,
        "channel_id": Globals.CHANNEL_ID,
        "message_flags": 0,
        "message_id": message_id,
        "application_id": "936929561302675456",
        "session_id": "1f3dbdf09efdf93d81a3a6420882c92c",
        "data": {
            "component_type": 2,
            "custom_id": f"MJ::JOB::reroll::0::{message_hash}::SOLO",
        },
    }

    headers = {"authorization": Globals.SALAI_TOKEN}
    return requests.post("https://discord.com/api/v9/interactions", json=payload, headers=headers)


def variation(index: int, message_id: str, message_hash: str, isSolo: bool) -> requests.Response:
    """
    Sends a request to the self bot to generate a new image with variations.

    Args:
        index (int): The index of the image to be generated.
        message_id (str): The ID of the message containing the image.
        message_hash (str): The hash of the message containing the image.
        isSolo (bool): Whether the image is a solo variation or not.

    Returns:
        requests.Response: The response from the self bot.
    """

    if isSolo:
        custom_id = f"MJ::JOB::variation::{index}::{message_hash}::SOLO"
    else:
        custom_id = f"MJ::JOB::variation::{index}::{message_hash}"

    payload = {
        "type": 3,
        "guild_id": Globals.SERVER_ID,
        "channel_id": Globals.CHANNEL_ID,
        "message_flags": 0,
        "message_id": message_id,
        "application_id": "936929561302675456",
        "session_id": "1f3dbdf09efdf93d81a3a6420882c92c",
        "data": {
            "component_type": 2,
            "custom_id": f"{custom_id}",
        },
    }

    headers = {"authorization": Globals.SALAI_TOKEN}
    return requests.post("https://discord.com/api/v9/interactions", json=payload, headers=headers)


def soloInteraction(message_id: str, message_hash: str, job: str) -> requests.Response:
    """
    Sends a request to the self bot for a solo interaction.

    Args:
        message_id (str): The ID of the message containing the image.
        message_hash (str): The hash of the message containing the image.
        job (str): The job to be performed by the self bot.

    Returns:
        requests.Response: The response from the self bot.
    """

    payload = {
        "type": 3,
        "guild_id": Globals.SERVER_ID,
        "channel_id": Globals.CHANNEL_ID,
        "message_flags": 0,
        "message_id": message_id,
        "application_id": "936929561302675456",
        "session_id": "1f3dbdf09efdf93d81a3a6420882c92c",
        "data": {
            "component_type": 2,
            "custom_id": f"MJ::JOB::{job}::1::{message_hash}::SOLO",
        },
    }

    headers = {"authorization": Globals.SALAI_TOKEN}
    return requests.post("https://discord.com/api/v9/interactions", json=payload, headers=headers)