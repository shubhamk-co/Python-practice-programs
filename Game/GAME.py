import sqlite3
import tkinter as tk
from tkinter import messagebox

# Initialize the database
def init_db():
    conn = sqlite3.connect('game.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            attack INTEGER,
            defense INTEGER,
            speed INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def add_player():
    try:
        pid = int(entry_id.get())
        name = entry_name.get()
        atk = int(entry_attack.get())
        defn = int(entry_defense.get())
        spd = int(entry_speed.get())

        conn = sqlite3.connect('game.db')
        c = conn.cursor()
        c.execute("INSERT INTO players VALUES (?, ?, ?, ?, ?)", (pid, name, atk, defn, spd))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "🧙 Player added to squad!")
        clear_entries()
    except:
        messagebox.showerror("Error", "❌ Invalid input or duplicate ID!")

def view_players():
    conn = sqlite3.connect('game.db')
    c = conn.cursor()
    c.execute("SELECT * FROM players")
    rows = c.fetchall()
    result_box.delete("1.0", tk.END)
    for row in rows:
        result_box.insert(tk.END, f"🎮 ID:{row[0]} | {row[1]} → ATK:{row[2]} DEF:{row[3]} SPD:{row[4]}\n")
    conn.close()

def delete_player():
    try:
        pid = int(entry_id.get())
        conn = sqlite3.connect('game.db')
        c = conn.cursor()
        c.execute("DELETE FROM players WHERE id = ?", (pid,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted", "💀 Player removed from game!")
        clear_entries()
    except:
        messagebox.showerror("Error", "❌ Invalid ID!")

def update_player():
    try:
        pid = int(entry_id.get())
        atk = int(entry_attack.get())
        defn = int(entry_defense.get())
        spd = int(entry_speed.get())
        conn = sqlite3.connect('game.db')
        c = conn.cursor()
        c.execute("""
            UPDATE players
            SET attack=?, defense=?, speed=?
            WHERE id=?
        """, (atk, defn, spd, pid))
        conn.commit()
        conn.close()
        messagebox.showinfo("Updated", "🛠️ Player stats upgraded!")
        clear_entries()
    except:
        messagebox.showerror("Error", "❌ Something went wrong!")

def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_attack.delete(0, tk.END)
    entry_defense.delete(0, tk.END)
    entry_speed.delete(0, tk.END)

# GUI Setup
init_db()
window = tk.Tk()
window.title("🎮 Player Stats Manager")
window.geometry("500x600")
window.configure(bg="#00FF91")

tk.Label(window, text="Player ID", bg="#B1FC01", fg="white").pack()
entry_id = tk.Entry(window)
entry_id.pack()

tk.Label(window, text="Player Name", bg="#4891FF", fg="white").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Attack", bg="#000000", fg="white").pack()
entry_attack = tk.Entry(window)
entry_attack.pack()

tk.Label(window, text="Defense", bg="#005EEA", fg="white").pack()
entry_defense = tk.Entry(window)
entry_defense.pack()

tk.Label(window, text="Speed", bg="#222831", fg="white").pack()
entry_speed = tk.Entry(window)
entry_speed.pack()

tk.Button(window, text="🎮 Add Player", command=add_player).pack(pady=5)
tk.Button(window, text="⚔️ Update Stats", command=update_player).pack(pady=5)
tk.Button(window, text="💀 Delete Player", command=delete_player).pack(pady=5)
tk.Button(window, text="📜 View All Players", command=view_players).pack(pady=5)

result_box = tk.Text(window, height=10, width=60)
result_box.pack(pady=10)

window.mainloop()