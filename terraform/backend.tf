terraform {
	backend "s3" {

          bucket = "gh1nanda"
          key    = "Terraform.tfstate"
          region = "us-east-1"	
	}
}
