# Message web controller.
class message_web_controller(object):
 
  # Constructor.
  def __init__(self):
    pass
 
  # HTTP get processor.
  def get(self,*args,**kwargs):
    if self.request=="/message/send":
      return render_template('message/send.html',var=self.var)
    elif self.request=="/messages":
      return render_template('message/list.html',var=self.var)