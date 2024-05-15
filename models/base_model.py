"""base_model.py"""
import uuid
from datetime import datetime
from models import storage

class BaseModel():
    """ defines all common attributes for other classes"""

    def __init__(self, *args, **kwargs):
        """Generate a unique ID for the instance"""

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)


    def __str__(self):
        """returns string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the updated_at attribute to current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """creates a dictionary representation"""
        obj_dict = self.__dict__.copy()

        """adds class name to dict"""
        obj_dict['__class__'] = self.__class__.__name__

        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
