from invoke import task
from elb import helpers

@task
def init(ctx, aws_account, aws_account_id, cluster, bucket_region):
    tf_config = (f'key="{cluster}-systemward-resources/{cluster}.tfstate"\n'\
                 f'bucket="systemward-{aws_account}-state"\n'\
                 f'region="{bucket_region}"\n'\
                  'profile="default"\n'\
                  'encrypt=1'\
                 f'kms_key_id="arn:aws:kms:{bucket_region}:{aws_account_id}:'\
                  'alias/{aws_account}-tf-state-kms-key"')
    with open('backend.conf', 'w') as f:
        f.write(tf_config)
    ctx.run('terraform init -backend-config ./backend.conf')


@task
def plan(ctx, environment):
    cmd = "terraform plan " \
          "-var-file=./{}.tfvars "

    ctx.run(cmd.format(environment))


@task
def apply(ctx, environment):
    cmd = "terraform apply " \
          "-auto-approve " \
          "-var-file=./{}.tfvars "

    ctx.run(cmd.format(environment))