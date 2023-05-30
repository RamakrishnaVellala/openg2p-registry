# Part of OpenG2P Registry. See LICENSE file for full copyright and licensing details.

import logging

from odoo import fields

# from odoo.tests import tagged
from odoo.tests.common import TransactionCase

_logger = logging.getLogger(__name__)


class MembershipTest(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(MembershipTest, cls).setUpClass()
        cls.env = cls.env(
            context=dict(
                cls.env.context,
                test_queue_job_no_delay=True,
            )
        )

        # Initial Setup of Variables
        cls.registrant_1 = cls.env["res.partner"].create(
            {
                "family_name": "Jaddranka",
                "given_name": "Heidi",
                "name": "Heidi Jaddranka",
                "is_group": False,
                "is_registrant": True,
            }
        )
        cls.registrant_2 = cls.env["res.partner"].create(
            {
                "family_name": "Kleitos",
                "given_name": "Angus",
                "name": "Angus Kleitos",
                "is_group": False,
                "is_registrant": True,
            }
        )
        cls.registrant_3 = cls.env["res.partner"].create(
            {
                "family_name": "Caratacos",
                "given_name": "Sora",
                "name": "Sora Caratacos",
                "is_group": False,
                "is_registrant": True,
            }
        )
        cls.registrant_4 = cls.env["res.partner"].create(
            {
                "family_name": "Demophon",
                "given_name": "Amaphia",
                "name": "Amaphia Demophon",
                "is_group": False,
                "is_registrant": True,
            }
        )
        cls.group_1 = cls.env["res.partner"].create(
            {
                "name": "Group 1",
                "is_group": True,
                "is_registrant": True,
            }
        )
        cls.group_2 = cls.env["res.partner"].create(
            {
                "name": "Group 2",
                "is_group": True,
                "is_registrant": True,
            }
        )
        cls.group_3 = cls.env["res.partner"].create(
            {
                "name": "Group 3",
                "is_group": True,
                "is_registrant": True,
            }
        )

    def test_01_add_members(self):
        self.group_1.write(
            {"group_membership_ids": [(0, 0, {"individual": self.registrant_1.id})]}
        )
        message = (
            "Membership Testing: Adding Group Member Failed! Result: %s Expecting: %s"
            % (
                self.group_1.group_membership_ids[0].individual.name,
                self.registrant_1.name,
            )
        )
        self.assertEqual(
            self.group_1.group_membership_ids[0].individual.id,
            self.registrant_1.id,
            message,
        )

    def test_02_assign_member(self):
        self.registrant_2.write(
            {"individual_membership_ids": [(0, 0, {"group": self.group_2.id})]}
        )
        message = (
            "Membership Testing: Assigning Member to Group Failed! Result %s Expecting %s"
            % (
                self.registrant_2.individual_membership_ids[0].group.id,
                self.group_2.id,
            )
        )
        self.assertEqual(
            self.registrant_2.individual_membership_ids[0].group.id,
            self.group_2.id,
            message,
        )

    def test_03_set_individual_to_disabled(self):
        """
        Disable an individual and modify its data.
        The test will run the write method of res.partner and execute the _recompute_parent_groups function.
        Modifying the disabled individual should raise an exception.
        :return:
        """
        _logger.info("Test 3: Set individual: %s to disabled." % self.registrant_3.name)
        curr_date = fields.Datetime.now()
        self.registrant_3.update(
            {
                "disabled": curr_date,
                "disabled_reason": "Disable reason",
                "disabled_by": self.env.user,
            }
        )
        self.assertEqual(
            self.registrant_3.disabled, curr_date, "Error disabling an individual"
        )

        _logger.info(
            "Test 4: Modify disabled individual: %s information. %s"
            % (self.registrant_3.name, self.registrant_3.disabled)
        )
        self.registrant_3.update(
            {
                "family_name": "Burito",
            }
        )
        self.assertEqual(
            self.registrant_3.family_name,
            "Burito",
            "Error modifying information of disabled individual",
        )
