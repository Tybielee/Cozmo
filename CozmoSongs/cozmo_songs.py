#!/usr/bin/env python3

import time

import cozmo

NoteTypes = cozmo.song.NoteTypes
"""
Shortened representation of the Cozmo NoteTypes to keep the code cleaner.
"""

NoteDurations = cozmo.song.NoteDurations
"""
Shortened representation of the Cozmo NoteDurations to keep the code cleaner.
"""


def add_song_note(note: NoteTypes, duration: NoteDurations) -> cozmo.song.SongNote:
    """
    Return a Cozmo SongNote based on the type of note and the duration of the note

    :param note:
        A musical note from C2 to C3 and the equivalent sharps
    :param duration:
        The duration of note defined by musical nomenclature
    :return:
        The SongNote created by the Anki Cozmo SDK
    """
    return cozmo.song.SongNote(note, duration)


def send_song_cozmo(notes, robot: cozmo.robot.Robot):
    """
    Dispatches the given array of SongNotes to the Cozmo Robot to play
    :param notes:
        An array of SongNotes.
    :param robot:
        The event dispatcher used in order to send the array to the connected robot.
    """

    time.sleep(0.5)
    robot.play_song(notes).wait_for_completed()


def cozmo_song_of_storms(robot: cozmo.robot.Robot):
    """
        Defines an array of SongNotes representing the Legend of Zelda's Song of Storms
        that are dispatched to the Cozmo Robot to play.
    :param robot:
        The event dispatcher used in order to send the array to the connected robot.
    """

    notes = [
        add_song_note(NoteTypes.D2, NoteDurations.Quarter),
        add_song_note(NoteTypes.F2, NoteDurations.Quarter),
        add_song_note(NoteTypes.D2, NoteDurations.Half),

        add_song_note(NoteTypes.D2, NoteDurations.Quarter),
        add_song_note(NoteTypes.F2, NoteDurations.Quarter),
        add_song_note(NoteTypes.D2, NoteDurations.Half),

        add_song_note(NoteTypes.E2, NoteDurations.ThreeQuarter),
        add_song_note(NoteTypes.G2, NoteDurations.Quarter),
        add_song_note(NoteTypes.F2, NoteDurations.Quarter),
        add_song_note(NoteTypes.G2, NoteDurations.Quarter),

        add_song_note(NoteTypes.F2, NoteDurations.Quarter),
        add_song_note(NoteTypes.C2, NoteDurations.Quarter),
        add_song_note(NoteTypes.A2, NoteDurations.Half),

        add_song_note(NoteTypes.A2, NoteDurations.Quarter),
        add_song_note(NoteTypes.D2, NoteDurations.Quarter),
        add_song_note(NoteTypes.F2, NoteDurations.Quarter),
        add_song_note(NoteTypes.G2, NoteDurations.Quarter),

        add_song_note(NoteTypes.A2, NoteDurations.Whole),

        add_song_note(NoteTypes.A2, NoteDurations.Quarter),
        add_song_note(NoteTypes.D2, NoteDurations.Quarter),
        add_song_note(NoteTypes.F2, NoteDurations.Quarter),
        add_song_note(NoteTypes.G2, NoteDurations.Quarter),

        add_song_note(NoteTypes.E2, NoteDurations.Whole),

        add_song_note(NoteTypes.D2, NoteDurations.Quarter),
        add_song_note(NoteTypes.F2, NoteDurations.Quarter),
        add_song_note(NoteTypes.D2, NoteDurations.Half),

        add_song_note(NoteTypes.D2, NoteDurations.Quarter),
        add_song_note(NoteTypes.F2, NoteDurations.Quarter),
        add_song_note(NoteTypes.D2, NoteDurations.Half),

        add_song_note(NoteTypes.E2, NoteDurations.ThreeQuarter),
        add_song_note(NoteTypes.G2, NoteDurations.Quarter),
        add_song_note(NoteTypes.F2, NoteDurations.Quarter),
        add_song_note(NoteTypes.G2, NoteDurations.Quarter),

        add_song_note(NoteTypes.F2, NoteDurations.Quarter),
        add_song_note(NoteTypes.C2, NoteDurations.Quarter),
        add_song_note(NoteTypes.A2, NoteDurations.Half),

        add_song_note(NoteTypes.A2, NoteDurations.Quarter),
        add_song_note(NoteTypes.D2, NoteDurations.Quarter),
        add_song_note(NoteTypes.F2, NoteDurations.Quarter),
        add_song_note(NoteTypes.G2, NoteDurations.Quarter),

        add_song_note(NoteTypes.A2, NoteDurations.Half),
        add_song_note(NoteTypes.A2, NoteDurations.Half),

        add_song_note(NoteTypes.D2, NoteDurations.Whole),
    ]
    """
        The notes array is broken up into bars (denoted by newlines) which are based on 4/4 time.
    """

    send_song_cozmo(notes, robot)


def cozmo_do_re_mi(robot: cozmo.robot.Robot):
    """
        Defines an array of SongNotes representing the song Do-Re-Mi that are dispatched to the Cozmo Robot to play.
    :param robot:
        The event dispatcher used in order to send the array to the connected robot.
    """

    notes = [
        add_song_note(NoteTypes.C2, NoteDurations.ThreeQuarter),
        add_song_note(NoteTypes.D2, NoteDurations.Quarter),

        add_song_note(NoteTypes.E2, NoteDurations.ThreeQuarter),
        add_song_note(NoteTypes.C2, NoteDurations.Quarter),

        add_song_note(NoteTypes.E2, NoteDurations.Half),
        add_song_note(NoteTypes.C2, NoteDurations.Half),

        add_song_note(NoteTypes.E2, NoteDurations.Half),
        add_song_note(NoteTypes.Rest, NoteDurations.Half),

        add_song_note(NoteTypes.D2, NoteDurations.ThreeQuarter),
        add_song_note(NoteTypes.E2, NoteDurations.Quarter),

        add_song_note(NoteTypes.F2, NoteDurations.Quarter),
        add_song_note(NoteTypes.F2, NoteDurations.Quarter),
        add_song_note(NoteTypes.E2, NoteDurations.Quarter),
        add_song_note(NoteTypes.D2, NoteDurations.Quarter),

        add_song_note(NoteTypes.F2, NoteDurations.Whole),
        add_song_note(NoteTypes.E2, NoteDurations.ThreeQuarter),
        add_song_note(NoteTypes.F2, NoteDurations.Quarter),

        add_song_note(NoteTypes.G2, NoteDurations.ThreeQuarter),
        add_song_note(NoteTypes.E2, NoteDurations.Quarter),

        add_song_note(NoteTypes.G2, NoteDurations.Half),
        add_song_note(NoteTypes.E2, NoteDurations.Half),

        add_song_note(NoteTypes.G2, NoteDurations.Half),
        add_song_note(NoteTypes.Rest, NoteDurations.Half),

        add_song_note(NoteTypes.F2, NoteDurations.ThreeQuarter),
        add_song_note(NoteTypes.G2, NoteDurations.Quarter),

        add_song_note(NoteTypes.A2, NoteDurations.Quarter),
        add_song_note(NoteTypes.A2, NoteDurations.Quarter),
        add_song_note(NoteTypes.G2, NoteDurations.Quarter),
        add_song_note(NoteTypes.F2, NoteDurations.Quarter),

        add_song_note(NoteTypes.A2, NoteDurations.Whole),
        add_song_note(NoteTypes.G2, NoteDurations.Half),
        add_song_note(NoteTypes.Rest, NoteDurations.Quarter),
        add_song_note(NoteTypes.C2, NoteDurations.Quarter),

        add_song_note(NoteTypes.D2, NoteDurations.Quarter),
        add_song_note(NoteTypes.E2, NoteDurations.Quarter),
        add_song_note(NoteTypes.F2, NoteDurations.Quarter),
        add_song_note(NoteTypes.G2, NoteDurations.Quarter),

        add_song_note(NoteTypes.A2, NoteDurations.Whole),

        add_song_note(NoteTypes.A2, NoteDurations.Half),
        add_song_note(NoteTypes.Rest, NoteDurations.Quarter),
        add_song_note(NoteTypes.D2, NoteDurations.Quarter),

        add_song_note(NoteTypes.E2, NoteDurations.Quarter),
        add_song_note(NoteTypes.F2_Sharp, NoteDurations.Quarter),
        add_song_note(NoteTypes.G2, NoteDurations.Quarter),
        add_song_note(NoteTypes.A2, NoteDurations.Quarter),

        add_song_note(NoteTypes.B2, NoteDurations.Whole),

        add_song_note(NoteTypes.B2, NoteDurations.Half),
        add_song_note(NoteTypes.Rest, NoteDurations.Quarter),
        add_song_note(NoteTypes.E2, NoteDurations.Quarter),

        add_song_note(NoteTypes.F2_Sharp, NoteDurations.Quarter),
        add_song_note(NoteTypes.G2_Sharp, NoteDurations.Quarter),
        add_song_note(NoteTypes.A2, NoteDurations.Quarter),
        add_song_note(NoteTypes.B2, NoteDurations.Quarter),

        add_song_note(NoteTypes.C3, NoteDurations.Whole),

        add_song_note(NoteTypes.Rest, NoteDurations.Half),
        add_song_note(NoteTypes.B2, NoteDurations.Quarter),
        add_song_note(NoteTypes.A2_Sharp, NoteDurations.Quarter),

        add_song_note(NoteTypes.A2, NoteDurations.Half),
        add_song_note(NoteTypes.F2, NoteDurations.Half),

        add_song_note(NoteTypes.B2, NoteDurations.Half),
        add_song_note(NoteTypes.G2, NoteDurations.Half),

        add_song_note(NoteTypes.C3, NoteDurations.Half),
        add_song_note(NoteTypes.Rest, NoteDurations.Half)
    ]
    """
        The notes array is broken up into bars (denoted by newlines) which are based on 4/4 time.
    """

    send_song_cozmo(notes, robot)
