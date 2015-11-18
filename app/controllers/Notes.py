from system.core.controller import *

class Notes(Controller):
  def __init__(self, action):
    super(Notes, self).__init__(action)
    self.load_model('Note')

  def index(self):
    notes = self.models['Note'].index()
    print notes
    return self.load_view('/notes/index.html', notes = notes)

  def create(self):
    self.models['Note'].create(request.form)
    return redirect('/')

  def update(self, id):
    self.models['Note'].update(request.form, id)
    return redirect('/')

  def delete(self, id):
    self.models['Note'].delete(id)
    return redirect('/')
