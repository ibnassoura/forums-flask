import copy
class BaseStore():

    def __init__(self,data_provider,last_id):
        self._data_provider=data_provider
        self._last_id=last_id

    def get_all(self):
        return self._data_provider

    def add(self, item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1

    def get_by_id(self,item_id):
        getlist=self._data_provider
        result=None
        for each in getlist:
            if each.id==item_id:
                result=each
                break
            return result

    def update(self,instance):
        getlist=self._data_provider

        for index,each in enumerate(getlist):
            if each.id==instance.id:
                getlist[index]=instance
                break

    def delete(self,id):
        getmember=self.get_by_id(id)
        self._data_provider.remove(getmember)

    def entity_exists(self,instance):
        getmembers=self.get_all()
        result=True
        if instance in getmembers:
            result=Flase
        return result

class MemberStore(BaseStore):
    members=[]
    last_id = 1

    def __init__(self):
        BaseStore.__init__(self,MemberStore.members, MemberStore.last_id)

    def get_by_name(self,name):
        all_members=self.get_all()
        result=[]
        for each in all_members:
            if each.name==name:
                result.append(each)
        return result
        
            
    def get_members_with_posts(self,all_posts):
        allmembers=copy.deepcopy(self.get_all())

        for member in allmembers:
            for post in all_posts:
                if member.id==post.member_id:
                    member.posts.append(post)
        return allmembers
            

    def get_top_two(self,members):

        newlist=sorted(self.get_members_with_posts(members),key=lambda x: len(x.posts),reverse=True)
        return newlist[:2]
        


class PostStore(BaseStore):
    posts=[]
    last_id=1

    def __init__(self):
        BaseStore.__init__(self,PostStore.posts, PostStore.last_id)

    def get_posts_by_date(self):
        allposts=copy.deepcopy(self.get_all())
        allposts=sorted(allposts,key=lambda x: x.date,reverse=True)
        for each in allposts:
            print each
        return allposts


        
                
        
        
            


        
