from system.core.router import routes

routes['default_controller']            = 'Notes'
routes['GET']['/Notes/delete/<id>']     = 'Notes#delete'
routes['POST']['/Notes/update/<id>']    = 'Notes#update'
routes['POST']['/Notes/create']         = 'Notes#create'
