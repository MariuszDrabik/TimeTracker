from repositories import ProjectRepository


class Project:
    def get_all(self):
        return [f'{i[0]} {i[1]}' for i in ProjectRepository().get_all()]
