import json
import uuid
from bson.objectid import ObjectId
obid= ObjectId()
mezua=''
courseid=''
erabid=''
commentid=str(uuid.uuid4())
erabiltzaile=''
commcount=2
titulo=''
f1= {'_id': str(obid), 'votes':{'up':[ ],'down':[ ],'up_count': 0, 'down_count': 0, 'count': 0, 'point': 0}, 'visible': 'true', 'abuse_flaggers':[ ],'historical_abuse_flaggers':[ ],"thread_type" : 'discussion', "comment_count" : commcount, 'at_position_list': [], 'title': titulo,
	"body" : mezua,
	"course_id" : courseid,
	"_type" : "CommentThread",
	"endorsed" : 'false',
	"anonymous" : 'false',
	"anonymous_to_peers" : 'false',
	"author_id" : erabid,
	"comment_thread_id" : commentid,
	"author_username" : erabiltzaile,
	"sk" : "5575dca756c02c8a01000003",
	"updated_at" : 'ISODate("2015-06-08T18:19:19.669Z")',
	"created_at" : 'ISODate("2015-06-08T18:19:19.669Z")'
}


with open("forum.json", "w") as outfile:
    json.dump(f1, outfile, indent=4)
