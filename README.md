# Deploy a Production Ready Portworx Cluster

## Quick Start

To deploy the cluster you can use Ansible

#### Installation Usage

```ShellSession
# Change working directory to the current repository
cd portworx-management

# Install dependencies from ``requirements.txt``
sudo pip3 install -r requirements.txt

# Prepare configuration file group_vars/all
vi group_vars/all

# Now we are ready to deploy the Portworx Cluster
# NOTE: oc tool will be downloaded if it isn't present on running host
#       playbook is executed on localhost
ansible-playbook cluster-install.yaml

Also installation supports tags which can customize installation
Tags:
  - check
  - pwx
  - grafana
  - postcheck
  - perf
  - report

For example:

#Check only prerequisites for installation
ansible-playbook cluster-install.yaml --tags=check

#Install only Portworx without any addition services like grafana
ansible-playbook cluster-install.yaml --tags=pwx

#Run cluster state, do performance tests, generate report
ansible-playbook cluster-install.yaml --tags='postcheck,perf,report'
```


#### Delete your Portworx Cluster

``` ShellSession
# In order to wipe your cluster with all the data on the disks you can run this Playbook
ansible-playbook remove-cluster.yaml

Also Deinstallation supports tags which can customize removing process
Tags:
  - pwx
  - grafana

For example:

#Remove only Grafana
ansible-playbook cluster-install.yaml --tags grafana
```

####TODO
- Add port verification between all nodes in a cluster (17001-17020). Needs to create two daemon sets. First open ports, second check availability.
- Add for AWS creds verification
- Add GCP platform
- Add IBM Cloud platform
- Add Vmware platform
- Add Kubernetes as a type of cluster
- Add support of local disks for nodes
- Add support of external kvdb
- Add support OCP4 Prometheus(partially implemented)
- Add support external Prometheus
