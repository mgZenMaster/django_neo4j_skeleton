from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    Relationship,
    UniqueIdProperty
)
from django_neomodel import DjangoNode


class Person(DjangoNode):

    node_id = UniqueIdProperty(primary_key=True)
    firstname = StringProperty()
    lastname = StringProperty()
    address = RelationshipTo('Address', 'LIVES_AT')

    class Meta:
        app_label = "myapp"

    @property
    def serialize(self):
        return {
            'node_properties': {
                'node_id': self.node_id,
                'firstname': self.firstname,
                'lastname': self.lastname,
            },
        }

    @property
    def serialize_connections(self):
        return [
            {
                'nodes_type': 'Address',
                'nodes_related': self.serialize_relationships(self.addresses.all()),
            },
        ]


class Address(DjangoNode):

    node_id = UniqueIdProperty(primary_key=True)
    city = StringProperty()

    class Meta:
        app_label = "myapp"

    @property
    def serialize(self):
        return {
            'node_properties': {
                'node_id': self.node_id,
                'city': self.city,
            },
        }
