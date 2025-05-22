import actions.home as home
import actions.clone as clone
import actions.init as init
import actions.destroy as destroy
import actions.user as user
import actions.commit as commit

class Actions:
    actionList = {
        "home": home,
        "clone": clone,
        "init": init,
        "destroy": destroy,
        "user": user,
        "commit": commit,
        # Add other actions here
    }