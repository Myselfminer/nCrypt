{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':u'nCrypt v. 0.1 alpha',
          'size':(400, 300),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'CheckBox', 
    'name':'ordnerNutzen', 
    'position':(148, 80), 
    'label':'Ordner Nutzen', 
    },

{'type':'StaticText', 
    'name':'Datei', 
    'position':(20, 80), 
    'text':'Datei', 
    },

{'type':'Button', 
    'name':'browse', 
    'position':(235, 99), 
    'size':(20, -1), 
    'label':'...', 
    },

{'type':'TextField', 
    'name':'path', 
    'position':(19, 100), 
    'size':(213, -1), 
    },

{'type':'Button', 
    'name':'Verschlsseln', 
    'position':(106, 48), 
    'label':'Verschlsseln', 
    },

{'type':'CheckBox', 
    'name':'altenCodeNutzen', 
    'position':(254, 130), 
    'label':'Alten Code nutzen', 
    },

{'type':'Button', 
    'name':'Entschlsseln', 
    'position':(20, 48), 
    'label':'Entschlsseln', 
    },

{'type':'StaticText', 
    'name':'Dictionary', 
    'position':(20, 128), 
    'text':'Dictionary', 
    },

{'type':'TextField', 
    'name':'dictionarypy', 
    'position':(20, 153), 
    'size':(342, -1), 
    'text':'../dictionary.py', 
    },

{'type':'StaticText', 
    'name':'Passwort', 
    'position':(20, 20), 
    'text':'Passwort', 
    },

{'type':'PasswordField', 
    'name':'passwort', 
    'position':(91, 18), 
    'text':'passwort', 
    },

{'type':'Gauge', 
    'name':'Gauge1', 
    'position':(20, 194), 
    'size':(344, 28), 
    'layout':'horizontal', 
    'max':100, 
    'value':0, 
    },

{'type':'StaticBox', 
    'name':'Tools', 
    'position':(258, 5), 
    'size':(117, 112), 
    'label':'Tools', 
    },

{'type':'Button', 
    'name':'neuesDict', 
    'position':(280, 20), 
    'label':'Neues Dict', 
    },

] # end components
} # end background
] # end backgrounds
} }
