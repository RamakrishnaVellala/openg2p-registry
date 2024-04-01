# Part of OpenG2P Registry. See LICENSE file for full copyright and licensing details.
{
    "name": "G2P Registry: Rest API",
    "category": "G2P",
    "version": "17.0.1.0.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": [
        "g2p_registry_base",
        "g2p_registry_group",
        "g2p_registry_individual",
        "fastapi",
        "extendable_fastapi",
    ],
    "external_dependencies": {"python": ["extendable-pydantic", "pydantic"]},
    "data": [
        "security/g2p_security.xml",
        "security/ir.model.access.csv",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
