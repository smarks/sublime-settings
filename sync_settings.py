import sublime
import sublime_plugin
import subprocess
import os


def plugin_loaded():
    """Run git pull when Sublime Text starts."""
    user_folder = os.path.dirname(__file__)

    def do_pull():
        try:
            result = subprocess.run(
                ["git", "pull", "--ff-only"],
                cwd=user_folder,
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                output = result.stdout.strip()
                if "Already up to date" not in output:
                    sublime.status_message("Settings synced: " + output.split('\n')[0])
            else:
                print(f"Settings sync failed: {result.stderr}")
        except Exception as e:
            print(f"Settings sync error: {e}")

    # Run after a short delay to not slow down startup
    sublime.set_timeout_async(do_pull, 1000)
