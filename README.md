# sw-k8s
This repo to be used to deploy a base k8s cluster


# Using build notifications with CircleCI and Slack

A context has been created in CircleCI which declares an oauth token for a Slackbot to notify the #sw-builds channel of *only* failed builds.

In order to use this, the following step needs to be included in a job:

      - slack/notify:
          channel: sw-builds
          event: fail
          template: basic_fail_1

In the event that environment variables ever need to be referenced (as stored in CircleCI), you must declare the context in the step of the CircleCI config.