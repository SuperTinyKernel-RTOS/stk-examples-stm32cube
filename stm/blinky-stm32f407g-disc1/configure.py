import subprocess
import os

def sparse_checkout(repo_url, repo_paths, local_dest, branch="main"):
    """
    repo_url: URL of the GitHub repo
    repo_paths: A list of internal repo paths (e.g., ['stk', 'build/example/driver'])
    local_dest: Where it should land locally (e.g., './deps')
    branch: The branch to pull from
    """
    base_dir = os.getcwd()
    target_path = os.path.abspath(local_dest)

    if not os.path.exists(target_path):
        os.makedirs(target_path)
    
    os.chdir(target_path)

    try:
        # Initialize Git if necessary
        if not os.path.exists(".git"):
            subprocess.run(["git", "init"], check=True)
            subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
            subprocess.run(["git", "config", "core.sparseCheckout", "true"], check=True)

        # Update the sparse-checkout list with all requested paths
        sparse_file = os.path.join(".git", "info", "sparse-checkout")
        with open(sparse_file, "w") as f:
            for path in repo_paths:
                f.write(f"{path}/\n")

        print(f"Syncing {repo_paths} into {local_dest} from branch '{branch}'...")
        # Pull the specific branch
        subprocess.run(["git", "pull", "origin", branch], check=True)
        
        print(f"Successfully updated {local_dest}\n")

    except subprocess.CalledProcessError as e:
        print(f"Error during checkout: {e}")
    finally:
        os.chdir(base_dir)

if __name__ == "__main__":
    REPO = "https://github.com/SuperTinyKernel-RTOS/stk"
    
    # 1. Pull the kernel AND the drivers to ./deps
    # Note: Using 'main' branch as both exist there in the latest repo structure
    deps_folders = ["stk", "build/example/driver"]
    sparse_checkout(REPO, deps_folders, "./deps", branch="main")
    
    # 2. Pull the blinky example to ./src
    sparse_checkout(REPO, ["build/example/blinky"], "./src", branch="main")