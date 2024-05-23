# Blackboard Learn API

## Get User ID: `GET`
```text
https://wlkc.ouc.edu.cn/learn/api/public/v1/users?userName={Student ID}
```

Sample:
```json
{
    "results": [
        {
            "id": "_xxxxx_x",
            "uuid": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "userName": "21020036048",
            "studentId": "S",
            "gender": "Unknown",
            "modified": "2024-05-22T06:28:29.000Z",
            "institutionRoleIds": [
                "STUDENT",
                "BbMobile"
            ],
            "systemRoleIds": [
                "User"
            ],
            "name": {
                "given": "鹿逸远",
                "family": "2021计算机科学与技术（中外合作办学）"
            },
            "avatar": {
                "viewUrl": "https://wlkc.ouc.edu.cn/learn/api/public/v1/users/_xxxxx_x/avatar",
                "source": "Default"
            }
        }
    ]
}
```

## Get Course List: `GET`
```text
https://wlkc.ouc.edu.cn/learn/api/public/v1/users/{User ID}/courses
```

Sample:
```json
{
  "results": [
    {
      "id": "_1878726_1",
      "userId": "_xxxxx_x",
      "courseId": "_27409_1",
      "dataSourceId": "_2_1",
      "created": "2024-02-19T02:54:42.000Z",
      "modified": "2024-02-19T02:54:42.000Z",
      "availability": {
        "available": "Yes"
      },
      "courseRoleId": "Student",
      "lastAccessed": "2024-04-24T13:18:12.000Z"
    }
  ]
}
```

## Get Contents: `GET`
```text
https://wlkc.ouc.edu.cn/learn/api/public/v1/courses/{Course ID}/contents
```

Sample:
```json
{
    "results": [
        {
            "id": "_825384_1",
            "title": "课程介绍",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:16:21.000Z",
            "position": 2,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825384_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825385_1",
            "title": "考核方式",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:32:43.000Z",
            "position": 4,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "No",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825385_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825386_1",
            "title": "教学日历",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:16:21.000Z",
            "position": 5,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825386_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825387_1",
            "title": "第一章 行列式",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:16:21.000Z",
            "position": 6,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825387_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825388_1",
            "title": "第二章 矩阵（新）",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:16:21.000Z",
            "position": 7,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825388_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825389_1",
            "title": "第三章 线性方程组（新）",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:16:21.000Z",
            "position": 8,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825389_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825390_1",
            "title": "第四章 向量空间与线性变换",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:16:21.000Z",
            "position": 9,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825390_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825391_1",
            "title": "第五章 特征值和特征向量 矩阵的对角化",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:16:21.000Z",
            "position": 10,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825391_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825392_1",
            "title": "第六章 二次型",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:16:21.000Z",
            "position": 11,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825392_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825393_1",
            "title": "作业",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:30:59.000Z",
            "position": 12,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825393_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825394_1",
            "title": "小专题讲解PPT",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:16:21.000Z",
            "position": 13,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "No",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825394_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825395_1",
            "title": "课外拓展",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:32:19.000Z",
            "position": 14,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "No",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825395_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825396_1",
            "title": "作业与测试",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-11-05T15:17:38.000Z",
            "position": 15,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825396_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825397_1",
            "title": "评分标准",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:31:59.000Z",
            "position": 16,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "No",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825397_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825398_1",
            "title": "在线学习",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:32:07.000Z",
            "position": 17,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "No",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825398_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825399_1",
            "title": "第一章 绪论",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:31:39.000Z",
            "position": 18,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "No",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825399_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825400_1",
            "title": "第二章 *******",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:31:45.000Z",
            "position": 19,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "No",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825400_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_825401_1",
            "title": "签到",
            "created": "2022-09-11T10:16:21.000Z",
            "modified": "2022-09-11T10:39:36.000Z",
            "position": 20,
            "hasChildren": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "No",
                "allowGuests": false,
                "allowObservers": false,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-folder"
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825401_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        }
    ]
}
```

## Get Content Detail
```text
https://wlkc.ouc.edu.cn/learn/api/public/v1/courses/{Course ID}/contents/{Content ID}/children
```

```json
{
    "results": [
        {
            "id": "_825546_1",
            "parentId": "_825393_1",
            "title": "作业W1",
            "body": "<p>p32,&nbsp; 2-4,&nbsp; 8-10</p>",
            "created": "2022-09-11T10:37:44.000Z",
            "modified": "2022-09-12T13:39:37.000Z",
            "position": 0,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_125832_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_825546_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_832938_1",
            "parentId": "_825393_1",
            "title": "作业W2",
            "body": "<p>P33: 11、13、14、19、20、23、25、40</p>",
            "created": "2022-09-16T11:37:18.000Z",
            "modified": "2022-09-16T11:37:18.000Z",
            "position": 1,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_126358_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_832938_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_837371_1",
            "parentId": "_825393_1",
            "title": "作业W3",
            "body": "<p>P33：16、17、29、31、32、35、39、48</p>",
            "created": "2022-09-23T09:01:30.000Z",
            "modified": "2022-09-23T09:01:30.000Z",
            "position": 2,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_126786_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_837371_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_839598_1",
            "parentId": "_825393_1",
            "title": "作业W4",
            "body": "<p>P93：1、4、6、9、10、15、16、18、20</p>",
            "created": "2022-09-30T09:09:06.000Z",
            "modified": "2022-09-30T09:09:06.000Z",
            "position": 3,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_127126_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_839598_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_842654_1",
            "parentId": "_825393_1",
            "title": "作业W5",
            "body": "<p>P95：22、28、29、36、37、39、40（2）（3）（6）</p>",
            "created": "2022-10-07T14:49:34.000Z",
            "modified": "2022-10-07T14:49:34.000Z",
            "position": 4,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_127624_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_842654_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_845451_1",
            "parentId": "_825393_1",
            "title": "作业W6",
            "body": "<p>19、45、46、47、67、69、83</p>",
            "created": "2022-10-14T08:36:34.000Z",
            "modified": "2022-10-14T08:36:34.000Z",
            "position": 5,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_128265_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_845451_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_846882_1",
            "parentId": "_825393_1",
            "title": "作业W7",
            "body": "<p>42、49、52、55、56、58、78、79</p>",
            "created": "2022-10-22T06:04:24.000Z",
            "modified": "2022-10-22T06:04:24.000Z",
            "position": 6,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_128585_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_846882_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_848069_1",
            "parentId": "_825393_1",
            "title": "作业W8",
            "body": "<p>59、60、62（1）（2）、82；</p> \n<p>P146  1、2、3</p>",
            "created": "2022-10-28T09:32:27.000Z",
            "modified": "2022-10-29T09:17:57.000Z",
            "position": 7,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_128860_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_848069_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_851362_1",
            "parentId": "_825393_1",
            "title": "作业W9",
            "body": "<p>P146： 4、7、10、45、48</p>",
            "created": "2022-11-06T08:46:36.000Z",
            "modified": "2022-11-06T08:46:36.000Z",
            "position": 8,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_129204_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_851362_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_855349_1",
            "parentId": "_825393_1",
            "title": "作业W10",
            "body": "<p>P147:  13 (2) (3)、14、19、21、23、49</p>",
            "created": "2022-11-11T09:14:35.000Z",
            "modified": "2022-11-14T04:51:45.000Z",
            "position": 9,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_129645_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_855349_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_856695_1",
            "parentId": "_825393_1",
            "title": "作业W11",
            "body": "<p>17、18、28（1）、29、32、37、38</p>",
            "created": "2022-11-18T10:53:42.000Z",
            "modified": "2022-11-18T10:53:55.000Z",
            "position": 10,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_129944_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_856695_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_857975_1",
            "parentId": "_825393_1",
            "title": "作业W12",
            "body": "<p>P149   30（2) (3);</p> \n<p>P210  1、2、3（1）、5、6、7</p>",
            "created": "2022-11-25T11:50:42.000Z",
            "modified": "2022-11-26T05:13:25.000Z",
            "position": 11,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_130269_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_857975_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_859113_1",
            "parentId": "_825393_1",
            "title": "作业W13",
            "body": "<p>P211：8（1）、9（2）、10、11、12；</p> \n<p>P247：1（4）（5）、29、30</p> \n<p><br></p>",
            "created": "2022-12-02T10:39:57.000Z",
            "modified": "2022-12-02T10:39:57.000Z",
            "position": 12,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_130542_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_859113_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_861771_1",
            "parentId": "_825393_1",
            "title": "作业W14",
            "body": "<p>P248：3、6、8、9、16（1）（2）（6）、20、39</p>",
            "created": "2022-12-10T05:59:14.000Z",
            "modified": "2022-12-10T05:59:14.000Z",
            "position": 13,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_130922_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_861771_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_863577_1",
            "parentId": "_825393_1",
            "title": "作业W15",
            "body": "<p>5.3 P249：24（1）（4）（5）、43、44、46（选择题需写出过程）</p> \n<p>6.1-6.2  P289:  2、4、8（2）、9、18、46</p>",
            "created": "2022-12-17T04:27:20.000Z",
            "modified": "2022-12-17T04:27:20.000Z",
            "position": 14,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_131251_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_863577_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        },
        {
            "id": "_865053_1",
            "parentId": "_825393_1",
            "title": "作业W16",
            "body": "<p>P291   21（1）（2）、22（3）、25（1）、29</p>",
            "created": "2022-12-29T10:01:05.000Z",
            "modified": "2023-01-04T06:09:17.000Z",
            "position": 15,
            "hasGradebookColumns": true,
            "launchInNewWindow": false,
            "reviewable": false,
            "availability": {
                "available": "Yes",
                "allowGuests": true,
                "allowObservers": true,
                "adaptiveRelease": {}
            },
            "contentHandler": {
                "id": "resource/x-bb-assignment",
                "gradeColumnId": "_131538_1",
                "groupContent": false,
                "originalityReportingTool": {
                    "id": "safeAssign",
                    "checkSubmission": false,
                    "studentViewReports": false,
                    "excludeSubmissionsFromDatabases": false
                }
            },
            "links": [
                {
                    "href": "/webapps/blackboard/execute/displayIndividualContent?course_id=_19874_1&content_id=_865053_1",
                    "rel": "alternate",
                    "title": "User Interface View",
                    "type": "text/html"
                }
            ]
        }
    ]
}
```

