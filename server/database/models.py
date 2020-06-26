from pymongo import MongoClient

import settings

client = MongoClient(settings.DB_URL)
database = client[settings.DB_NAME]


class Model:
    pk = None

    _pk_name = None
    _collection_name = None

    def as_dict(self):
        raise NotImplementedError

    @property
    def collection(self):
        return database[self._collection_name]

    def save(self):
        if self.pk:
            return self.update()
        return self.create()

    def create(self):
        saved_data = self.collection.insert_one(self.as_dict())
        self.pk = saved_data[self._pk_name]

    def update(self, **kwargs):
        return self.collection.update_one({self._pk_name: self.pk},
                                          {"$set", kwargs or self.as_dict()})

    def delete(self):
        return self.collection.delete_one({self._pk_name: self.pk})

    @classmethod
    def find(cls, **kwargs):
        collection = database[cls._collection_name]
        return collection.find(kwargs)
