#!/usr/bin/python

from .marker import run_loop
import click


@click.command()
@click.option("--token", help="Access token for vk api")
@click.option("--delay", default=60, help="Time between message polls in seconds")
@click.option("--also-mute", default="",
              help="Ids of chats and users whose messages also should be marked as read automatically. You can pass multiple ids by seperating them by colon")
def run(token, delay, additional_ban_list):
    run_loop(token, delay, additional_ban_list.split(","))


if __name__ == '__main__':
    run()
