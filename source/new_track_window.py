import tkinter
from tkinter import messagebox
import re


class NewTrackWindow(tkinter.Toplevel):
    def __init__(self, track):
        super().__init__()
        self.track = track
        self.features = None

        self.title_track_label = tkinter.Label(self, text=track, bg="white", fg="black")
        self.title_track_label.pack()

        self.danceability_var = tkinter.StringVar()
        self.energy_var = tkinter.StringVar()
        self.instrumentalness_var = tkinter.StringVar()
        self.tempo_var = tkinter.StringVar()
        self.valence_var = tkinter.StringVar()

        self.add_danceability_label = tkinter.Label(self, text="Enter danceability (0.000-0.999):", bg="white",
                                                    fg="black")
        self.add_danceability_label.pack()
        self.add_danceability_entry = tkinter.Entry(self, textvariable=self.danceability_var,
                                                    font=('calibre', 10, 'normal'))
        self.add_danceability_entry.pack()
        self.add_energy_label = tkinter.Label(self, text="Enter energy (0.000-0.999):", bg="white", fg="black")
        self.add_energy_label.pack()
        self.add_energy_entry = tkinter.Entry(self, textvariable=self.energy_var,
                                              font=('calibre', 10, 'normal'))
        self.add_energy_entry.pack()
        self.add_instrumentalness_label = tkinter.Label(self, text="Enter instrumentalness (0.000-0.999):", bg="white",
                                                        fg="black")
        self.add_instrumentalness_label.pack()
        self.add_instrumentalness_entry = tkinter.Entry(self, textvariable=self.instrumentalness_var,
                                                        font=('calibre', 10, 'normal'))
        self.add_instrumentalness_entry.pack()
        self.add_tempo_label = tkinter.Label(self, text="Enter tempo (0.000-245.000):", bg="white",
                                             fg="black")
        self.add_tempo_label.pack()
        self.add_tempo_entry = tkinter.Entry(self, textvariable=self.tempo_var,
                                             font=('calibre', 10, 'normal'))
        self.add_tempo_entry.pack()
        self.add_valence_label = tkinter.Label(self, text="Enter valence (0.000-0.999):", bg="white",
                                               fg="black")
        self.add_valence_label.pack()
        self.add_valence_entry = tkinter.Entry(self, textvariable=self.valence_var,
                                               font=('calibre', 10, 'normal'))
        self.add_valence_entry.pack()

        self.save_button = tkinter.Button(self, text="Save", font=("Helvetica", 10), command=self.save)
        self.save_button.pack(pady=5)

    def is_number_repl_isdigit(self, s):
        """ Returns True if string is a number. """
        return s.replace('.', '', 1).isdigit()

    def save(self):
        danceability = self.add_danceability_entry.get()
        energy = self.add_energy_entry.get()
        instrumentalness = self.add_instrumentalness_entry.get()
        tempo = self.add_tempo_entry.get()
        valence = self.add_valence_entry.get()

        if (len(danceability) == 0 or len(energy) == 0 or
                len(instrumentalness) == 0 or len(tempo) == 0 or
                len(valence) == 0):
            return messagebox.showwarning("Warning", "Empty fields")

        flag1 = self.is_number_repl_isdigit(danceability)
        flag2 = self.is_number_repl_isdigit(energy)
        flag3 = self.is_number_repl_isdigit(instrumentalness)
        flag4 = self.is_number_repl_isdigit(tempo)
        flag5 = self.is_number_repl_isdigit(valence)

        if not flag1:
            return messagebox.showwarning("Warning", "Wrong fields")
        if not flag2:
            return messagebox.showwarning("Warning", "Wrong fields")
        if not flag3:
            return messagebox.showwarning("Warning", "Wrong fields")
        if not flag4:
            return messagebox.showwarning("Warning", "Wrong fields")
        if not flag5:
            return messagebox.showwarning("Warning", "Wrong fields")


        self.features = {
            'danceability': danceability,
            'energy': energy,
            'instrumentalness': instrumentalness,
            'tempo': tempo,
            'valence': valence
        }

        self.destroy()
