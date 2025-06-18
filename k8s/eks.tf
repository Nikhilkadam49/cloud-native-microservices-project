module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "20.8.4"

  cluster_name    = var.cluster_name
  cluster_version = "1.29"
  subnet_ids      = module.vpc.private_subnets
  vpc_id          = module.vpc.vpc_id

  eks_managed_node_group_defaults = {
    ami_type = "ami-020cba7c55df1f615"
  }

  eks_managed_node_groups = {
    default = {
      min_size     = 1
      max_size     = 2
      desired_size = 2

      instance_types = ["t2.xlarge"]
    }
  }

  tags = {
    Terraform = "true"
    Project   = "cloud-native"
  }
}
