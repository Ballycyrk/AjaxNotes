from system.core.model import Model

class Note(Model):
  def __init__(self):
    super(Note, self).__init__()

  def index(self):
    get = "SELECT * FROM notes"
    return self.db.query_db(get)

  def create(self, note):
    insert = "INSERT INTO notes(title, content, created_at, updated_at) VALUES (%s, %s, NOW(), NOW())"
    data = (note['title'], note['content'])
    return self.db.query_db(insert, data)

  def delete(self, id):
    delete  = "DELETE FROM notes WHERE id = %s"
    data    = [id]
    return self.db.query_db(delete, data)

  def update(self, note, id):
    update = "UPDATE notes SET content = %s, updated_at = NOW() WHERE id = %s"
    data = (note['content'], int(id))

    return self.db.query_db(update, data)
