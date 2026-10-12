"""Managed private replay stack for project 'gitops-hub'.

Written by config0 write-back. Do not edit: the next write-back
overwrites it. Every step names a folder of REPOSITORY at
PAYLOAD_COMMIT; the payload commit is the commit before this one.
"""

REPOSITORY = "williaumwu/config0-e2e-gitops"
PAYLOAD_COMMIT = "442e9009d96a3b8a3d764ff10b939e1f43692d51"
STEPS = [
    {
        "depends_on": [],
        "folder": "main-570017720022/570017720022/ap-northeast-1/gitops-hub/vpc/vpc_simple/03dd8318ef1719a9",
        "kind": "terraform",
        "name": "main-570017720022/570017720022/ap-northeast-1/gitops-hub/vpc/vpc_simple/03dd8318ef1719a9"
    },
    {
        "depends_on": [
            "main-570017720022/570017720022/ap-northeast-1/gitops-hub/vpc/vpc_simple/03dd8318ef1719a9"
        ],
        "folder": "main-570017720022/570017720022/ap-northeast-1/gitops-hub/vpc/sg_3tier/43eb24a3bf9939fe",
        "kind": "terraform",
        "name": "main-570017720022/570017720022/ap-northeast-1/gitops-hub/vpc/sg_3tier/43eb24a3bf9939fe"
    },
    {
        "depends_on": [
            "main-570017720022/570017720022/ap-northeast-1/gitops-hub/vpc/sg_3tier/43eb24a3bf9939fe"
        ],
        "folder": "main-570017720022/570017720022/ap-northeast-1/gitops-hub/bucket/buckets/666dd2658186eed9",
        "kind": "terraform",
        "name": "main-570017720022/570017720022/ap-northeast-1/gitops-hub/bucket/buckets/666dd2658186eed9"
    }
]


class Main(newSchedStack):

    def __init__(self, stackargs):
        newSchedStack.__init__(self, stackargs)
        self.parse.add_required(key="replay_project_id", types="str")
        self.parse.add_required(key="replay_project_name", types="str")
        self.parse.add_required(key="owner_id", types="str")
        self.parse.add_required(key="request_id", types="str")

    def run_step_1(self):
        self.stack.init_variables()
        step = STEPS[0]
        import shlex

        parts = [
            'config0', 'gitops', 'pipeline-run',
            f"project_id={self.stack.replay_project_id}",
            f"project_name={self.stack.replay_project_name}",
            f"owner_id={self.stack.owner_id}",
            'action=apply',
            f"request_id={self.stack.request_id}",
        ]
        self.stack.add_external_cmd(
            cmd=' '.join(shlex.quote(part) for part in parts),
            role='gitops/tenant/execute',
            human_description="replay terraform: 3 folders in dependency order",
            display=True)
        return True

    def run(self):
        self.add_job("step_1")
        return self.finalize_jobs()

    def schedule(self):
        sched = self.new_schedule()
        sched.job = "step_1"
        sched.archive.timeout = 4800
        sched.human_description = "replay terraform pipeline"
        self.add_schedule()

        return self.get_schedules()
