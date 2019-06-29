from helpers.test_helper import CustomTestCase
from rest_framework.test import APITestCase

from .serializers import DataFileSerializer


class DataFileSerializerTest(CustomTestCase, APITestCase):

    def setUp(self):
        self.required_fields = ['file_name', 'file_type']
        self.not_required_fields = ['url', 'date_loaded', 'created',
                                    'updated', 'loaded_by', 'upload']

    def test_fields(self):
        serializer = DataFileSerializer()
        self.assert_fields_required(True, serializer, self.required_fields)
        self.assert_fields_required(False, serializer,
                                    self.not_required_fields)
        self.assertEqual(len(serializer.fields),
                         len(self.required_fields) +
                         len(self.not_required_fields))
