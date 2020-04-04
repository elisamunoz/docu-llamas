from bson.objectid import ObjectId

# MongoDB Collections
def coll_categories(db):
    return db.categories.find()
def coll_patterns(db):
    return db.patterns.find()
def coll_difficulty(db):
    return db.difficulty.find()

# MongoDB Getters
def pattern(db, id):
    return db.patterns.find_one({"_id": ObjectId(id)})
def pattern_count(db):
    return db.patterns.estimated_document_count()
