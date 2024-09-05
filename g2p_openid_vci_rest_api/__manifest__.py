{
    "name": "G2P OpenID VCI: Rest API",
    "category": "G2P",
    "version": "17.0.0.0.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "LGPL-3",
    "depends": [
        "g2p_openid_vci",
        "fastapi",
        "extendable_fastapi",
    ],
    "external_dependencies": {"python": ["extendable-pydantic", "pydantic", "jq"]},
    "data": ["data/fastapi_endpoint_vci.xml"],
    "assets": {
        "web.assets_backend": [],
        "web.assets_qweb": [],
    },
    "demo": [],
    "images": [],
    "application": False,
    "installable": True,
    "auto_install": False,
}
