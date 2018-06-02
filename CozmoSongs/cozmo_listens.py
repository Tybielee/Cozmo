#!/usr/bin/env python3

# This file is based on work done by raproence (Github)
# https://gist.github.com/raproenca/ed1ab47c47da246512ef4d2f19cf2611
# Removed definitions that were currently not needed for my purposes.
# Renamed many functions and variables for more clarity from the original
# Added documentation not existing in the original.
# Extended by adding a Sing command to sing the songs previously created.
# Extended by adding an Exit command rather than relying on keyboard input.

# pip3 install SpeechRecognition
# pip3 install PyAudio

import random
import sys

import cozmo
import speech_recognition as sr

from cozmo_songs import cozmo_do_re_mi, cozmo_song_of_storms

command_activate = "Cosmo"
"""
The command to activate Cozmo's listening skills, Cozmo is recognized as Cosmo.
"""

command_speak = "say"
"""
The command to activate Cozmo's ability to repeat phrases 
"""

command_exit = "exit"
"""
The command to exit the application.
"""

command_sing = "sing"
"""
The command to activate Cozmo's singing.
"""


def cozmo_speaks(recognized, robot):
    """
        Sends a speech event to the Cozmo robot if there were words to repeat besides the command words.

        Example:
        "Cozmo say" would print an Index error.
        "Cozmo say hello" would send the word hello to the cozmo robot to repeat.
    :param recognized:
        The string version of the audio input that was created by the recognizer.
    :param robot:
        The event dispatcher used in order to send the array to the connected robot.
    """
    try:
        line = recognized.split(' ', 2)[2]
        robot.say_text(line).wait_for_completed()
        print("Cozmo said: %s" % line)

    except IndexError:
        print("You did not give Cozmo anything to repeat.")


def cozmo_sings(robot):
    """
        Sends a song to the connected Cozmo based on the random number generated.
    :param robot:
        The event dispatcher used in order to send the array to the connected robot.
    """

    if random.randint(0, 99) > 50:
        cozmo_do_re_mi(robot)
    else:
        cozmo_song_of_storms(robot)


def cozmo_listens(speech_input, recognizer, robot):
    """
        Listens for audio input and then determines if the command given matches any of Cozmo's known commands.
    :param speech_input:
        The audio data received from the microphone.
    :param recognizer:
        An object that contains speech recognition functionality
    :param robot:
        The event dispatcher used in order to send the array to the connected robot.
    """
    audio = recognizer.listen(speech_input)
    try:
        recognized = recognizer.recognize_google(audio)
        print("You said: " + recognized)
        if command_activate in recognized or command_activate.lower() in recognized:
            if command_speak in recognized:
                cozmo_speaks(recognized, robot)

            elif command_exit in recognized:
                exit(0)

            elif command_sing in recognized or command_sing.lower() in recognized:
                cozmo_sings(robot)

            else:
                print("Command not recognized.")

        else:
            print("Please start all commands with the word, " + command_activate)

    except sr.UnknownValueError:
        print("Speech Recognition could not understand you.")
    except sr.RequestError as exception:
        print("Could not request results from Google Speech Recognition service; {0}".format(exception))


def run(robot: cozmo.robot.Robot):
    """
        This method runs once the Cozmo SDK is connected.
    :param robot:
        The event dispatcher used in order to send the array to the connected robot.
    """
    try:
        print("Please provide Cozmo a command.")
        recognizer = sr.Recognizer()
        with sr.Microphone() as speechInput:
            while 1:
                cozmo_listens(speechInput, recognizer, robot)
                print("Please Try Again.")

    except KeyboardInterrupt:
        print("Exit requested by user")


if __name__ == "__main__":
    cozmo.setup_basic_logging()
    try:
        cozmo.run_program(run)
    except cozmo.ConnectionError as e:
        sys.exit("A connection error occurred: %s" % e)
