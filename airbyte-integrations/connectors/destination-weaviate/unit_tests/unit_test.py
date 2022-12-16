#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#
from unittest.mock import Mock

from destination_weaviate.client import Client


def test_client_custom_vectors_config():
    mock_object = Client
    mock_object.get_weaviate_client = Mock(return_value=None)
    c = Client({"vectors": "my_table.test", "url": "http://test"}, schema={})
    assert c.vectors["my_table"] == "test", "Single vector should work"

    c = Client({"vectors": "case2.test, another_table.vector", "url": "http://test"}, schema={})
    assert c.vectors["case2"] == "test", "Multiple values case2 should work too"
    assert c.vectors["another_table"] == "vector", "Multiple values another_table should work too"


def test_client_custom_id_schema_config():
    mock_object = Client
    mock_object.get_weaviate_client = Mock(return_value=None)
    c = Client({"id_schema": "my_table.my_id", "url": "http://test"}, schema={})
    assert c.id_schema["my_table"] == "my_id", "Single id_schema definition should work"

    c = Client({"id_schema": "my_table.my_id, another_table.my_id2", "url": "http://test"}, schema={})
    assert c.id_schema["my_table"] == "my_id", "Multiple values should work too"
    assert c.id_schema["another_table"] == "my_id2", "Multiple values should work too"
