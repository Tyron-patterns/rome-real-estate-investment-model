university_areas = {

    # PUBLIC UNIVERSITIES
    "Sapienza": {
        "type": "public",
        "core": [
            "San Lorenzo",
            "Policlinico",
            "Piazza Bologna",
            "Nomentano",
            "Verano"
        ],
        "nearby": [
            "Tiburtina (near station)",
            "Casal Bertone",
            "Portonaccio"
        ],
        "extended": [
            "Pigneto",
            "Re di Roma",
            "Monti Tiburtini",
            "Furio Camillo"
        ]
    },

    "Roma Tre": {
        "type": "public",
        "core": [
            "Ostiense",
            "Garbatella",
            "San Paolo"
        ],
        "nearby": [
            "Marconi",
            "Testaccio",
            "Piramide"
        ],
        "extended": [
            "Portuense",
            "Monteverde",
            "EUR (north edge)"
        ]
    },

    "Tor Vergata": {
        "type": "public",
        "core": [
            "Tor Vergata",
            "Romanina"
        ],
        "nearby": [
            "Anagnina",
            "Cinecittà",
            "Don Bosco"
        ],
        "extended": [
            "Appio Claudio",
            "Tuscolana (far)"
        ]
    },


    # PRIVATE UNIVERSITIES
    "LUISS": {
        "type": "private",
        "core": [
            "Parioli",
            "Trieste",
            "Salario"
        ],
        "nearby": [
            "Nomentano",
            "Pinciano"
        ],
        "extended": [
            "Flaminio"
        ]
    },

    "Cattolica (Gemelli)": {
        "type": "private",
        "core": [
            "Monte Mario",
            "Gemelli",
            "Trionfale"
        ],
        "nearby": [
            "Balduina",
            "Pineta Sacchetti"
        ],
        "extended": [
            "Prati (far edge)"
        ]
    },

    "UNINT": {
        "type": "private",
        "core": [
            "EUR",
            "Laurentina"
        ],
        "nearby": [
            "Garbatella (far)",
            "San Paolo (far)"
        ],
        "extended": []
    },

    "Università Europea di Roma": {
        "type": "private",
        "core": [
            "Aurelia",
            "Bravetta"
        ],
        "nearby": [
            "Monteverde"
        ],
        "extended": []
    },

    "Link Campus": {
        "type": "private",
        "core": [
            "Monteverde",
            "Gianicolense"
        ],
        "nearby": [
            "Trastevere"
        ],
        "extended": []
    },


    # INTERNATIONAL UNIVERSITIES
    "John Cabot": {
        "type": "international",
        "core": [
            "Trastevere",
            "Gianicolo"
        ],
        "nearby": [
            "Testaccio"
        ],
        "extended": [
            "Monteverde"
        ]
    },

    "American University of Rome": {
        "type": "international",
        "core": [
            "Trastevere",
            "Gianicolo"
        ],
        "nearby": [
            "Monteverde"
        ],
        "extended": []
    },


    # SPECIALIZED INSTITUTES
    "IED (Design)": {
        "type": "specialized",
        "core": [
            "San Giovanni",
            "Testaccio",
            "Ostiense"
        ],
        "nearby": [
            "Pigneto",
            "Re di Roma"
        ],
        "extended": []
    },

    "Accademia Belle Arti": {
        "type": "specialized",
        "core": [
            "Flaminio",
            "Parioli",
            "Centro Storico"
        ],
        "nearby": [
            "Prati"
        ],
        "extended": []
    }

}

#####

area_university_list = [

    # Sapienza core
    ["San Lorenzo", "Sapienza", "core", "public"],
    ["Policlinico", "Sapienza", "core", "public"],
    ["Piazza Bologna", "Sapienza", "core", "public"],
    ["Nomentano", "Sapienza", "core", "public"],
    ["Verano", "Sapienza", "core", "public"],

    # Sapienza nearby
    ["Tiburtina (near station)", "Sapienza", "nearby", "public"],
    ["Casal Bertone", "Sapienza", "nearby", "public"],
    ["Portonaccio", "Sapienza", "nearby", "public"],

    # Sapienza extended
    ["Pigneto", "Sapienza", "extended", "public"],
    ["Re di Roma", "Sapienza", "extended", "public"],
    ["Monti Tiburtini", "Sapienza", "extended", "public"],
    ["Furio Camillo", "Sapienza", "extended", "public"],


    # Roma Tre core
    ["Ostiense", "Roma Tre", "core", "public"],
    ["Garbatella", "Roma Tre", "core", "public"],
    ["San Paolo", "Roma Tre", "core", "public"],

    # Roma Tre nearby
    ["Marconi", "Roma Tre", "nearby", "public"],
    ["Testaccio", "Roma Tre", "nearby", "public"],
    ["Piramide", "Roma Tre", "nearby", "public"],

    # Roma Tre extended
    ["Portuense", "Roma Tre", "extended", "public"],
    ["Monteverde", "Roma Tre", "extended", "public"],
    ["EUR (north edge)", "Roma Tre", "extended", "public"],


    # Tor Vergata
    ["Tor Vergata", "Tor Vergata", "core", "public"],
    ["Romanina", "Tor Vergata", "core", "public"],
    ["Anagnina", "Tor Vergata", "nearby", "public"],
    ["Cinecittà", "Tor Vergata", "nearby", "public"],
    ["Don Bosco", "Tor Vergata", "nearby", "public"],
    ["Appio Claudio", "Tor Vergata", "extended", "public"],


    # LUISS
    ["Parioli", "LUISS", "core", "private"],
    ["Trieste", "LUISS", "core", "private"],
    ["Salario", "LUISS", "core", "private"],
    ["Nomentano", "LUISS", "nearby", "private"],
    ["Pinciano", "LUISS", "nearby", "private"],


    # Cattolica (Gemelli)
    ["Monte Mario", "Cattolica", "core", "private"],
    ["Gemelli", "Cattolica", "core", "private"],
    ["Trionfale", "Cattolica", "core", "private"],
    ["Balduina", "Cattolica", "nearby", "private"],
    ["Pineta Sacchetti", "Cattolica", "nearby", "private"],


    # UNINT
    ["EUR", "UNINT", "core", "private"],
    ["Laurentina", "UNINT", "core", "private"],


    # Università Europea
    ["Aurelia", "Università Europea", "core", "private"],
    ["Bravetta", "Università Europea", "core", "private"],
    ["Monteverde", "Università Europea", "nearby", "private"],


    # Link Campus
    ["Monteverde", "Link Campus", "core", "private"],
    ["Gianicolense", "Link Campus", "core", "private"],
    ["Trastevere", "Link Campus", "nearby", "private"],


    # International universities
    ["Trastevere", "John Cabot", "core", "international"],
    ["Gianicolo", "John Cabot", "core", "international"],
    ["Testaccio", "John Cabot", "nearby", "international"],

    ["Trastevere", "AUR", "core", "international"],
    ["Gianicolo", "AUR", "core", "international"],
    ["Monteverde", "AUR", "nearby", "international"],


    # Specialized institutes
    ["San Giovanni", "IED", "core", "specialized"],
    ["Testaccio", "IED", "core", "specialized"],
    ["Ostiense", "IED", "core", "specialized"],
    ["Pigneto", "IED", "nearby", "specialized"],
    ["Re di Roma", "IED", "nearby", "specialized"],

    ["Flaminio", "Accademia Belle Arti", "core", "specialized"],
    ["Parioli", "Accademia Belle Arti", "core", "specialized"],
    ["Centro Storico", "Accademia Belle Arti", "core", "specialized"],
    ["Prati", "Accademia Belle Arti", "nearby", "specialized"]

]