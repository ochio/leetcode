import json
import os
import re
import sys

import requests

GRAPHQL_URL = "https://leetcode.com/graphql"
query = """\
query questionData($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        questionId
        title
        translatedTitle
        codeDefinition
        content
        translatedContent
        difficulty
        likes
        dislikes
        similarQuestions
        topicTags {
            name
            slug
            translatedName
            __typename
        }
        codeSnippets {
            lang
            langSlug
            code
            __typename
        }
        stats
        hints
        exampleTestcases
        sampleTestCase
        metaData
        enableRunCode
    }
}
"""


def getQuestionTitle(url):
    pattern = re.compile('(?<=https://leetcode.com/problems/)[^/]*', )
    title = re.search(pattern, url)
    return title.group()


def fetchQuestion(title):
    variables = {'titleSlug': title}
    r = requests.get(GRAPHQL_URL, json={
                     'query': query, 'variables': variables})
    return r.json()


def getTargetTemplate(data):
    template_format = json.loads(data['data']['question']['codeDefinition'])
    filtered_data = list(
        filter(lambda lang: lang['value'] == 'python3', template_format))
    if len(filtered_data) != 1:
        raise ValueError("取得したデータが正しくありません")
    return filtered_data[0]['defaultCode']


def createSolutionFile(dirname, code, fileName="solution.py"):
    if not (os.path.exists(dirname)):
        os.mkdir(dirname)
    try:
        with open(f'{dirname}/{fileName}', "x") as f:
            f.write(code)
            print('\033[32m' + f'{dirname}/{fileName} を作成しました。' + '\033[0m')
    except FileExistsError:
        print('\033[31m' + f'{dirname}/{fileName} が既に存在します。' + '\033[0m')


def init():
    args = sys.argv
    title = getQuestionTitle(args[1])
    try:
        data = fetchQuestion(title)
        python_template = getTargetTemplate(data)
        createSolutionFile(title, python_template)
    except:
        createSolutionFile(title, "", fileName="solution.sql")


if __name__ == '__main__':
    init()
