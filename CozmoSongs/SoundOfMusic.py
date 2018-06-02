import time
import cozmo

NoteTypes = cozmo.song.NoteTypes
NoteDurations = cozmo.song.NoteDurations

def add_song_note(note: cozmo.song.NoteTypes, duration: cozmo.song.NoteDurations):

    return cozmo.song.SongNote(note, duration)

def cozmo_odetojoy(robot: cozmo.robot.Robot):
    notes = [
        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Half)]
    time.sleep(0.5)
    robot.play_song(notes, loop_count=1).wait_for_completed()
    notes = [
        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.Rest, cozmo.song.NoteDurations.Half) ]

    robot.play_song(notes, loop_count=1).wait_for_completed()


def cozmo_songofstorms(robot: cozmo.robot.Robot):
    notes = [
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Half),

        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Half),

        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.ThreeQuarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),

        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),

        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),

        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Whole),

        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),

        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Whole),

        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Half),

        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Half),

        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.ThreeQuarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),

        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),

        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),

        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),

        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Whole),
    ]
    time.sleep(0.5)
    robot.play_song(notes, loop_count=1).wait_for_completed()


def cozmo_do_re_mi(robot: cozmo.robot.Robot):
    stanza1 = [
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
    ]

    stanza2 = [
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
    ]

    stanza3 = [
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
    ]

    stanza4 = [
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

    time.sleep(0.5)
    robot.play_song(stanza1).wait_for(timeout=5)
    robot.play_song(stanza2).wait_for_completed()
    robot.play_song(stanza3).wait_for_completed()
    robot.play_song(stanza4).wait_for_completed()


# cozmo.run_program(cozmo_odetojoy)

# cozmo.run_program(cozmo_songofstorms)

cozmo.run_program(cozmo_do_re_mi)