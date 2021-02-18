class HostCreate:

    @staticmethod
    def setup(workers, laptop):

        remote_host = laptop

        Console.info("Setting up eth to wifi bridge.")
        os.system("cms bridge create --interface='wlan0'")
        Console.info("Creating keys on workers")
        os.system(f"cms host key create {workers}")
        Console.info("Gathering keys from workers, and remote host")
        os.system(f"cms host key gather {workers},{remote_host}"
                  f"keys.txt")
        Console.info("Scattering keys to manager and workers.")
        os.system(f"cms host key scatter {workers},localhost keys.txt")
        os.system("rm keys.txt")
        Console.info("Setting up ssh tunnels to workers through manager")
        os.system(f"cms host tunnel create {workers}")