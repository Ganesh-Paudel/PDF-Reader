import sqlite3
import hashlib
import os

class DatabaseManager:
    def __init__(self, db_name="reader_data.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pdf_notes (
                fileHash TEXT PRIMARY KEY,
                filePath TEXT,
                pre_notes TEXT,
                last_page INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()

    def _generate_hash(self, filePath):
        if not os.path.exists(filePath):
            return None
        with open(filePath, "rb") as f:
            return hashlib.md5(f.read(1024)).hexdigest()

    def save_note(self, filePath, noteText):
        fileHash = self._generate_hash(filePath)
        self.cursor.execute('''
            INSERT INTO pdf_notes (fileHash, filePath, pre_notes)
            VALUES (?, ?, ?)
            ON CONFLICT(fileHash) DO UPDATE SET pre_notes=excluded.pre_notes
        ''', (fileHash, filePath, noteText))
        self.conn.commit()

    def get_note(self, filePath):
        fileHash = self._generate_hash(filePath)
        self.cursor.execute('SELECT pre_notes FROM pdf_notes WHERE fileHash = ?', (fileHash,))
        result = self.cursor.fetchone()
        return result[0] if result else ""
