class Folder(Base, UnicodeMixIn):
    root = Column(Boolean, default = False)
    path = Column(Unicode(4096))
    created = Column(DateTime, default = now)
    last_scan = Column(DateTime, default = now)

    parent_id = Column(ForeignKey('folder.id', ondelete="CASCADE"))
    parent = relationship("Folder", remote_side=[id])

    @hybrid_property
    def name(self):
        return os.path.basename(self.path)

    def get_children(self):
        return self.mp.query_children().all()

    def as_subsonic_child(self, user):
        info = {
            'id': self.id,
            'isDir': True,
            'title': self.name,
            'album': self.name,
            'created': self.created.isoformat()
        }
        if not self.root and self.parent:
            info['parent'] = self.parent.id
            info['artist'] = self.parent.name
        info['coverArt'] = self.id

        starred = session.query(StarredFolder).get((user.id, self.id))
        if starred:
            info['starred'] = starred.date.isoformat()

        rating = session.query(RatingFolder).get((user.id, self.id))
        if rating:
            info['userRating'] = rating.rating
            avgRating = session.query(RatingFolder).filter(RatingFolder.rated_id == self.id).value(func.avg(RatingFolder.rating))
            if avgRating:
                info['averageRating'] = avgRating

        return info