## /////////////////////////////////////////////////////////////////////////////
## TESTING AREA
## THIS IS AN AREA WHERE YOU CAN TEST YOUR WORK AND WRITE YOUR TESTS
## /////////////////////////////////////////////////////////////////////////////

from rest_framework.test import APITestCase, RequestsClient

from ..models.player import Player
from ..models.player_skill import PlayerSkill

class CreatePlayerTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Player.objects.all().delete()
        PlayerSkill.objects.all().delete()

    def test_sample(self):
        data = {
            'name': 'player name',
            'position': 'goalkeeper',
            'playerSkills': [
                {
                    'skill': 'attack',
                    'value': 60
                },
                {
                    'skill': 'speed',
                    'value': 80
                }
            ]
        }

        response = self.client.post('http://testserver/api/player', data=data, format='json')
        self.assertIsNotNone(response)
