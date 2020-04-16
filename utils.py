from bson.objectid import ObjectId

# MongoDB Collections
def find_categories(db):
    return db.categories.find()
def find_patterns(db):
    return db.patterns.find()
def find_difficulty(db):
    return db.difficulty.find()

# MongoDB Getters
def get_pattern(db, id):
    return db.patterns.find_one({"_id": ObjectId(id)})
def get_pattern_count(db):
    return db.patterns.estimated_document_count()
