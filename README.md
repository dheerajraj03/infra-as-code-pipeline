@'
# Infrastructure as Code Pipeline

Automated application deployment using Terraform,
GitHub Actions, Amazon ECR, Amazon ECS Fargate,
an Application Load Balancer, and CloudWatch.

## Project goals

- Provision AWS infrastructure using Terraform modules
- Validate, test, and build application code
- Deploy changes to staging automatically
- Require approval for production deployment
- Verify application health and support rollback

## Repository structure

- app/: Application and Docker configuration
- terraform/: Infrastructure as Code
- .github/workflows/: CI/CD workflows
- docs/: Architecture, runbook, and cost estimates
'@ | Set-Content README.md