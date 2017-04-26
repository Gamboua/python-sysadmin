import jenkins


class JenkinsManager:
    def __init__(self):
        try:
            self.server = jenkins.Jenkins("http://jenkins.dexter.com.br:8080/")
        except Exception as e:
            raise Exception(e)

    def getVersion(self):
        try:
            return self.server.get_version()
        except Exception as e:
            raise Exception(e)

    def createJob(self):
        return self.server.create_job('Python Job teste', jenkins.EMPTY_CONFIG_XML)


if __name__ == '__main__':
    try:
        jenkins = JenkinsManager()
        print jenkins.getVersion()
        jenkins.createJob()
    except Exception as e:
        print e
