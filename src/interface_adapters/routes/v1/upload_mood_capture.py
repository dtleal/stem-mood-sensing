from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from domain.use_cases.upload_mood_capture import UploadMoodCaptureUseCase
from frameworks.container import FrameworkContainer
from interface_adapters.dtos.upload_mood_capture import (
    UploadMoodCaptureInputDTO,
    UploadMoodCaptureOutputDTO,
)

upload_mood_capture_route = APIRouter()


@upload_mood_capture_route.post(
    "/mood/upload/", response_model=UploadMoodCaptureOutputDTO
)
@inject
async def upload_mood_capture(
    input_dto: UploadMoodCaptureInputDTO,
    use_case: UploadMoodCaptureUseCase = Depends(
        Provide[FrameworkContainer.upload_mood_capture_use_case]
    ),
) -> UploadMoodCaptureOutputDTO:
    """Route to upload a user mood"""
    try:
        input_use_case = UploadMoodCaptureInputDTO(
            user_name=input_dto.user_name,
            mood=input_dto.mood,
            location=input_dto.location,
        )

        output_use_case = await use_case(input_use_case=input_use_case)

        return UploadMoodCaptureOutputDTO(
            user_id=output_use_case.user_id,
            user_name=output_use_case.user_name,
            mood=output_use_case.mood,
            location=output_use_case.location,
        )
    except Exception as error:
        return {"error": f"{error}"}
