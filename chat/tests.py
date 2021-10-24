from django.test import TestCase

from .models import Room

class HomePageTest(TestCase):
    def test_all_rooms_are_rendered_in_homepage(self):
        Room.objects.create(
            name='room 1',
            slug='room-1',
            description='This is the 1st room'
        )
        Room.objects.create(
            name='room 2',
            slug='room-2',
            description='This is the 2nd room'
        )

        response = self.client.get('/')

        self.assertContains(response, 'room 1')
        self.assertContains(response, 'room 2')

class RoomDetailTest(TestCase):

    def test_room_details_are_present_in_room_page(self):
        room_1 = Room.objects.create(
            name='room X',
            slug='room-x',
            description='This is the X-room'
        )

        response = self.client.get('/rooms/{}/'.format(room_1.slug))

        self.assertContains(response, room_1.name)
        self.assertContains(response, room_1.description)