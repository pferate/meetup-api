# MEETUP API Methods
[Source](https://www.meetup.com/meetup_api/docs/)

##v3 abuse

    GET /self/blocks/:member_id
    POST /self/blocks/:member_id
    POST /self/abuse_reports
    POST /:urlname/abuse_reports
    DELETE /self/blocks/:member_id

##v3 batch

    POST /batch

##v3 boards

    GET /:urlname/boards
    GET /:urlname/boards/:bid/discussions
    GET /:urlname/boards/:bid/discussions/:did

##v2 categories

    GET /2/categories

##v2 cities

    GET /2/cities

##v3 comments

    GET /:urlname/events/:event_id/comments

##v2 dashboard

    GET /dashboard

##v3 events

    GET /:urlname/events/:id/attendance
    POST /:urlname/events/:id/attendance
    GET /self/events
    GET /:urlname/events/:id
    POST /:urlname/events/:id/payments
    POST /:urlname/events/:id/watchlist
    DELETE /:urlname/events/:id/watchlist
    GET /:urlname/events

##v2 events

    GET /2/open_events
    GET /2/concierge
    GET /2/events
    POST /2/event
    POST /2/event/:id
    DELETE /2/event/:id
    GET /2/event_comments
    POST /2/event_comment
    GET /2/event_comment/:id
    DELETE /2/event_comment/:id
    POST /2/event_comment_flag
    DELETE /2/event_comment_subscribe/:id
    POST /2/event_comment_subscribe/:id
    POST /2/event_comment_like/:id
    DELETE /2/event_comment_like/:id
    GET /2/event_comment_likes
    GET /2/event_ratings
    POST /2/event_rating

##v1 feeds

    GET /activity

##v3 groups

    GET /find/groups
    GET /:urlname
    POST /:urlname
    POST /:urlname/topics
    DELETE /:urlname/topics
    GET /recommended/groups
    POST /recommended/groups/ignores/:urlname
    GET /:urlname/similar_groups

##v2 groups

    GET /2/groups
    POST /2/group_photo

##v1 groups

    GET /comments

##v2 members

    GET /2/members
    GET /2/member/:id
    POST /2/member/:id
    DELETE /2/member_photo/:id
    POST /2/member_photo

##v3 meta

    GET /status

##v3 notifications

    GET /notifications
    POST /notifications/read

##v1 oembed

    GET /oembed

##v3 photos

    GET /:urlname/photo_albums/:album_id/photos
    GET /:urlname/events/:event_id/photos
    GET /:urlname/events/:event_id/photos/:photo_id
    POST /:urlname/events/:event_id/photos
    GET /:urlname/photo_albums/:album_id
    DELETE /:urlname/events/:event_id/photos/:photo_id/comments/:comment_id

##v2 photos

    DELETE /2/photo/:id
    POST /2/photo/:id
    GET /2/photo_comments
    POST /2/photo_comment
    GET /2/photo_albums
    GET /2/photos
    POST /2/photo_album
    POST /2/photo

##v3 pro

    GET /pro/:urlname/groups
    GET /pro/:urlname/members

##v3 profiles

    POST /:urlname/member/approvals
    DELETE /:urlname/member/approvals
    GET /members/:member_id
    PATCH /members/:member_id
    POST /:urlname/members
    GET /:urlname/members/:member_id
    PATCH /:urlname/members/:member_id

##v2 profiles

    GET /2/profiles
    POST /2/profile
    POST /2/profile/:gid/:mid
    GET /2/profile/:gid/:mid
    DELETE /2/profile/:gid/:mid

##v2 rsvps

    GET /2/rsvps
    POST /2/rsvp
    GET /2/rsvp/:id

##v2 streams

    GET /2/rsvps
    WS /2/rsvps
    GET /2/rsvps
    GET /2/open_events
    GET /2/photos
    WS /2/photos
    GET /2/photos
    GET /2/open_venues
    GET /2/event_comments
    WS /2/event_comments
    GET /2/event_comments

##v3 topics

    GET /recommended/group_topics

##v2 topics

    GET /2/topic_categories

##v1 topics

    GET /topics

##v3 venues

    GET /:urlname/venues
    GET /recommended/venues
    POST /:urlname/venues

##v2 venues

    GET /2/open_venues
    GET /2/venues

