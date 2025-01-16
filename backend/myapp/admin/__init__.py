from django.contrib import admin
from ..models import *

from .owner_admin import OwnerAdmin
from .activity_admin import ActivityAdmin
from .contact_admin import ContactAdmin
from .illustration_admin import IllustrationAdmin
from .pseudoname_admin import PseudoNameAdmin
from .repository_admin import RepositoryAdmin
from .skill_admin import SkillAdmin
from .tag_admin import TagAdmin
from .video_admin import VideoAdmin

from .image_of import *
from .tag_of import *

admin.site.register(Owner, OwnerAdmin)
admin.site.register(ActivityImage, ActivityImageAdmin)
admin.site.register(RepositoryImage, RepositoryImageAdmin)
admin.site.register(IllustrationTag, IllustrationTagAdmin)
admin.site.register(RepositoryTag, RepositoryTagAdmin)
admin.site.register(VideoTag, VideoTagAdmin)
admin.site.register(SkillTag, SkillTagAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Illustration, IllustrationAdmin)
admin.site.register(PseudoName, PseudoNameAdmin)
admin.site.register(Repository, RepositoryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Video, VideoAdmin)

