{
    "name": "G2P Registration Portal :Base",
    "category": "G2P",
    "version": "17.0.1.4.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "depends": [
        "g2p_agent_portal_base",
        "g2p_registry_membership",
        "g2p_enumerator",
        "website",
    ],
    "data": [
        "views/base.xml",
        "views/dashboard.xml",
        "views/error_page.xml",
        "views/group_template.xml",
        "views/success_page.xml",
        "views/individual_page.xml",
        "views/login.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "g2p_registration_portal_base/static/src/css/style.css",
        ],
        "web.assets_common": [],
        "website.assets_wysiwyg": [],
    },
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
