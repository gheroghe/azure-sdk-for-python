[CmdletBinding(SupportsShouldProcess = $true)]
param(
  [Parameter(Mandatory = $true)]
  [string]$Organization,

  [Parameter(Mandatory = $true)]
  [string]$Project,

  [Parameter(Mandatory = $true)]
  [string]$SourceBranch,

  [Parameter(Mandatory = $true)]
  [int]$DefinitionId,

  [Parameter(Mandatory = $false)]
  [string]$QueuedPipelines,

  [Parameter(Mandatory = $true)]
  [string]$AuthToken
)

. "${PSScriptRoot}\logging.ps1"

$headers = @{
  Authorization = "Basic $AuthToken"
}

$apiUrl = "https://dev.azure.com/$Organization/$Project/_apis/build/builds?api-version=6.0"

$body = @{
  sourceBranch = $SourceBranch
  definition = @{ id = $DefinitionId }
}

Write-Verbose ($body | ConvertTo-Json)

try {
  $resp = Invoke-RestMethod -Method POST -Headers $headers $apiUrl -Body ($body | ConvertTo-Json) -ContentType application/json
}
catch {
  LogError "Invoke-RestMethod $apiUrl failed with exception:`n$_"
  exit 1
}

LogDebug "Pipeline [ $($resp.definition.name) ] queued at [ $($resp._links.web.href) ]"

if ($QueuedPipelines -or ($QueuedPipelines -eq 'not-yet-set')) {
  LogDebug $QueuedPipelines
  $QueuedPipelineLinks += "$QueuedPipelines\n[$($resp.definition.name)]($($resp._links.web.href))"
  Write-Host "##vso[task.setvariable variable=QueuedPipelines]$QueuedPipelineLinks"
}

